// Navigation only; artifact content, drafts and explicit decisions belong to the host.
export function mountReviewDesk(root,{getItems,renderArtifact,initialId,onNavigate=()=>{},breakpoint=760}) {
  const media=matchMedia(`(max-width: ${breakpoint}px)`);
  const items=()=>getItems();
  const find=id=>items().find(x=>x.id===id);
  const type=x=>/^problem statement$/i.test(x.artifactType||'')?'Problem':x.artifactType||x.title;
  const label=x=>items().filter(y=>type(y)===type(x)).length>1?`${type(x)} · ${x.title}`:type(x);
  const route=()=>new URLSearchParams(location.hash.slice(1)).get('review');
  const first=()=>items().find(x=>x.needsReview!==false)?.id||items()[0]?.id||null;
  let selected=find(route())?.id||find(initialId)?.id||first();
  function write(id,push=false){const url=new URL(location.href);const hash=new URLSearchParams(url.hash.slice(1));id?hash.set('review',id):hash.delete('review');url.hash=hash.toString();history[push?'pushState':'replaceState']({},'',url);}
  function render(focus=false){
    root.className=`review-desk${media.matches?' rd-mobile':''}`;root.replaceChildren();
    const queue=document.createElement('nav');queue.className='rd-queue';queue.setAttribute('aria-label','Review artifacts');
    for(const item of items()){const button=document.createElement('button');button.type='button';button.dataset.artifactId=item.id;if(item.id===selected)button.setAttribute('aria-current','page');const title=document.createElement('span');title.textContent=label(item);const status=document.createElement('small');status.textContent=item.status||'Needs review';button.append(title,status);button.onclick=()=>api.select(item.id);queue.append(button)}
    root.append(queue);
    const panel=document.createElement('section');panel.className='rd-artifact';const item=find(selected);
    if(item){panel.setAttribute('aria-label',label(item));panel.append(renderArtifact(item,api));}
    else{const h=document.createElement('h1');h.textContent=items().length?'Ready to send':'No artifacts to review';const p=document.createElement('p');p.textContent=items().length?'Send your feedback to continue.':'';panel.append(h,p);}
    root.append(panel);
    if(focus){const h=panel.querySelector('h1,h2,h3')||panel;h.tabIndex=-1;h.focus({preventScroll:true});window.scrollTo(0,0);}
    queue.querySelector('[aria-current]')?.scrollIntoView({block:'nearest',inline:'nearest'});
  }
  function navigate(id,push=true){selected=id;write(id,push);onNavigate({id,view:id?'detail':'complete'});render(true)}
  const back=()=>{selected=find(route())?.id||first();onNavigate({id:selected,view:'detail'});render(true)};
  const resize=()=>render();
  const api={select(id){if(find(id))navigate(id)},showQueue(){navigate(first())},advance(){const all=items();const start=all.findIndex(x=>x.id===selected);let next=null;for(let step=1;step<=all.length;step++){const x=all[(start+step+all.length)%all.length];if(x.needsReview!==false){next=x.id;break}}navigate(next)},refresh(){render()},destroy(){window.removeEventListener('popstate',back);media.removeEventListener('change',resize);root.replaceChildren()}};
  write(selected);window.addEventListener('popstate',back);media.addEventListener('change',resize);render();return api;
}
