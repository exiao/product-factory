import {mountReviewDesk} from './assets/review-desk.js';
const config=await fetch('./artifacts.json').then(r=>r.json());
const key=a=>`${a.id}:v${a.version}`;
const storageKey=config.storageKey||`artifact-review:${config.id}`;
const status=document.querySelector('#status');
const send=document.querySelector('#send');
document.querySelector('#project-title').textContent=config.title;document.title=config.title;
let state={drafts:{},responses:{},requests:[],selected:null};
try{state={...state,...JSON.parse(localStorage.getItem(storageKey)||'{}')}}catch{status.textContent='Could not restore browser drafts.'}
let connected=false;
try{
  const [saved,cap]=await Promise.all([fetch('/api/review').then(r=>r.json()),fetch('/api/capabilities').then(r=>r.json())]);connected=cap.dispatch===true;
  for(const group of ['drafts','responses'])for(const[k,v]of Object.entries(saved[group]||{})){if(!state[group][k]||(v.at||'')>(state[group][k].at||''))state[group][k]=v}
  state.requests=[...new Map([...(saved.requests||[]),...state.requests].map(x=>[x.id||JSON.stringify(x),x])).values()];
  if((saved.selectedAt||'')>(state.selectedAt||'')){state.selected=saved.selected;state.selectedAt=saved.selectedAt}
}catch{status.textContent='Connection unavailable. Your drafts are still editable.'}
send.textContent=connected?'Send to Codex':'Save feedback';
function local(){try{localStorage.setItem(storageKey,JSON.stringify(state))}catch{status.textContent='Browser storage is unavailable. Use the send button before closing.'}}
function payload(){return {...state,project:config.title,artifacts:config.artifacts.map(({id,version,type})=>({id,version,type}))}}
async function post(endpoint){const r=await fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload())});const data=await r.json();if(!r.ok)throw Error(data.error||'Could not save. Your notes are preserved.');return data}
const labels={keep:'Kept',direction:'Selected',revision:'Revision requested',dismiss:'Archived'};
function items(){return config.artifacts.map(a=>{const response=state.responses[key(a)];return{id:a.id,artifactType:a.type,title:a.title,status:labels[response?.intent]||a.status||'Needs review',needsReview:!response&&!a.settled}})}
function node(tag,text,cls){const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e}
function safeUrl(value){try{const u=new URL(value,location.href);return /^https?:$/.test(u.protocol)?u.href:null}catch{return null}}
function link(label,url){const a=node('a',label);const href=safeUrl(url);if(href){a.href=href;a.target='_blank';a.rel='noopener noreferrer'}return a}
function render(item,nav){const a=config.artifacts.find(x=>x.id===item.id),k=key(a);const draft=state.drafts[k]||{notes:'',directions:a.selected||[]};const choices=new Set(draft.directions||[]);const actionDrafts=draft.actions||{};const root=node('article');root.append(node('h1',a.question||a.title));
  if(a.image){const fig=node('figure','',`artifact-media${a.prototype?' prototype':''}`);const img=node('img');img.src=safeUrl(a.image)||'';img.alt=a.alt||a.title;fig.append(img);root.append(fig);if(a.prototype){const tools=node('div','','media-tools');const launch=link('Open prototype',a.prototype);launch.className='button primary';tools.append(launch);root.insertBefore(tools,fig)}}
  if(a.limitation)root.append(node('p',a.limitation,'limitation'));
  if(a.content){const content=node('div','',a.options?.length?'read-content comparison-content':'read-content');for(const paragraph of a.content){const p=node('p',typeof paragraph==='string'?paragraph:paragraph.text);for(const ref of paragraph.references||[]){p.append(document.createTextNode(' '),link(ref.label,ref.url))}content.append(p)}if(a.points){const ul=node('ul');for(const text of a.points)ul.append(node('li',text));content.append(ul)}root.append(content)}
  if(a.options?.length){const group=node('div','','choices');for(const option of a.options){const label=node('label');const input=node('input');input.type=a.singleSelection?'radio':'checkbox';input.name='direction';input.value=option.id;input.checked=choices.has(option.id);input.onchange=()=>{if(a.singleSelection)choices.clear();input.checked?choices.add(option.id):choices.delete(option.id);saveDraft()};label.append(input,node('span',option.label));group.append(label)}root.append(group)}
  const label=node('label','Notes or changes','feedback-label');label.htmlFor='notes';const notes=node('textarea');notes.id='notes';notes.value=draft.notes||'';notes.placeholder='What would you change?';root.append(label,notes);
  function saveDraft(){state.drafts[k]={notes:notes.value,directions:[...choices],actions:actionDrafts,at:new Date().toISOString()};local();send.disabled=false;send.textContent=connected?'Send to Codex':'Save feedback'}notes.oninput=saveDraft;
  const message=node('p','','card-status');message.setAttribute('role','status');root.append(message);
  const footer=node('footer','','review-footer');const position=node('span',`${config.artifacts.indexOf(a)+1} / ${config.artifacts.length}`,'position');const actions=node('div','','actions');const revise=node('button','Request revision');const keep=node('button',a.options?.length?'Keep selection →':'Keep →','primary');actions.append(revise,keep);footer.append(position,actions);root.append(footer);
  async function respond(intent){saveDraft();if(intent==='revision'&&!notes.value.trim()){message.textContent='Describe the change you want.';notes.focus();return}if(intent==='direction'&&!choices.size&&!notes.value.trim()){message.textContent='Select an option or describe your direction.';notes.focus();return}const old=state.responses[k];state.responses[k]={artifact:a.id,version:a.version,intent,notes:notes.value,directions:[...choices],at:new Date().toISOString()};keep.disabled=revise.disabled=true;message.textContent='Saving…';try{await post('/api/review');local();nav.advance()}catch(e){old?state.responses[k]=old:delete state.responses[k];message.textContent=e.message;keep.disabled=revise.disabled=false}}
  keep.onclick=()=>respond(a.options?.length?'direction':'keep');revise.onclick=()=>respond('revision');
  return root;
}
const desk=mountReviewDesk(document.querySelector('#review'),{getItems:items,initialId:state.selected,renderArtifact:render,onNavigate:({id})=>{state.selected=id;state.selectedAt=new Date().toISOString();local()}});
send.onclick=async()=>{send.disabled=true;status.textContent='Sending…';try{const result=await post(connected?'/api/submit':'/api/snapshot');if(result.status==='queued'){status.textContent='Sent to Codex.';send.textContent='Sent'}else{status.textContent='Saved locally. Codex is not connected.';send.disabled=false}}catch(e){status.textContent=e.message;send.disabled=false}};
