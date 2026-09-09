/* Original classroom implementation: simplified logit cognitive hierarchy. */
function coordinationModel(tau=1.5,gamma=1.2,safe=5,K=16){
 if(!(tau>=0&&tau<=5&&gamma>=1&&gamma<=2&&safe>0&&safe<8&&K>=1&&K<=32)) throw Error('Parameters outside classroom model domain');
 let w=[Math.exp(-tau)],levels=[[.5,.5]];
 for(let k=1;k<=K;k++)w.push(w[k-1]*tau/k);
 for(let k=1;k<=K;k++){
  let z=0,q=0;for(let h=0;h<k;h++){z+=w[h];q+=w[h]*levels[h][0];}q/=z;
  let a=gamma**k*8*q,b=gamma**k*(7*q+safe*(1-q));let d=Math.max(a,b);
  let ea=Math.exp(a-d),eb=Math.exp(b-d);levels.push([ea/(ea+eb),eb/(ea+eb)]);
 }
 let mass=w.reduce((a,b)=>a+b,0),p=w.reduce((v,a,k)=>v+a*levels[k][0],0)/mass;
 let uC=8*p,uS=7*p+safe*(1-p),u=p*uC+(1-p)*uS;
 return {p,levels,tail:Math.max(0,1-mass),regret:Math.max(uC,uS)-u,mixed:safe/(1+safe),uC,uS};
}
if(typeof module!=='undefined')module.exports={coordinationModel};
