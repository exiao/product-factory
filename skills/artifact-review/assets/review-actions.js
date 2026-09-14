// Mount once per active artifact. Host owns persistence and further-work execution.
export function mountReviewActions(container,{onAction,extension='option'}={}){
 const bar=document.createElement('div');bar.className='ar-actions';
 for(const [kind,label] of [[extension,extension==='research'?'Request research':'Request new option'],['comment','Add comment'],['dismiss','Dismiss']]){
  const button=document.createElement('button');button.type='button';button.textContent=label;
  button.onclick=()=>{if(kind==='dismiss'){onAction({kind});return}open(button,kind)};bar.append(button);
 }
 let popup;const drafts={};
 function close(){const trigger=popup?._trigger;popup?.remove();popup=null;trigger?.focus()}
 function open(trigger,kind){close();popup=document.createElement('section');popup.className='ar-popover';popup._trigger=trigger;popup.setAttribute('role','dialog');popup.setAttribute('aria-label',trigger.textContent);
 const input=document.createElement('textarea');input.setAttribute('aria-label',kind==='comment'?'Comment':'Request details');input.placeholder=kind==='comment'?'Your comment…':'What should we explore?';
 input.value=drafts[kind]||'';input.oninput=()=>drafts[kind]=input.value;
 const status=document.createElement('p');status.setAttribute('role','status');
 const submit=document.createElement('button');submit.type='button';submit.textContent=kind==='comment'?'Save comment':'Save request';
 submit.onclick=async()=>{if(kind==='comment'&&!input.value.trim()){input.focus();return}submit.disabled=true;try{await onAction({kind,text:input.value.trim()});delete drafts[kind];close()}catch{status.textContent='Could not save. Your text is still here.';submit.disabled=false}};
 const cancel=document.createElement('button');cancel.type='button';cancel.textContent='Cancel';cancel.onclick=close;
 popup.append(input,status,submit,cancel);popup.onkeydown=e=>{if(e.key==='Escape'){e.preventDefault();close()}};container.append(popup);const rect=trigger.getBoundingClientRect();popup.style.left=Math.max(16,Math.min(innerWidth-popup.offsetWidth-16,rect.left))+'px';popup.style.top=Math.max(16,Math.min(innerHeight-popup.offsetHeight-16,rect.bottom+8))+'px';input.focus();
 }
 container.append(bar);return ()=>{popup?.remove();bar.remove()};
}
