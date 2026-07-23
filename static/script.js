const botao=document.getElementById("botao-teste");
const elDownload=document.getElementById("download");
const elUpload=document.getElementById("upload");
const elStatus=document.getElementById("status");

async function rodarteste(){
    botao.disabled=true;
    botao.textContent="Testando...";
    elStatus.textContent="Isso pode levar alguns segundos, aguarde...";
    elDownload.textContent="--";
    elUpload.textContent="--";

    try{
        const resposta=await fetch("/api/speedtest");
        const dados=await resposta.json();

        if(!resposta.ok){
            throw new Error(dados.error || "Erro desconhecido");
        }

        elDownload.textContent=dados.download_mbps;
        elUpload.textContent=dados.upload_mbps;
        elStatus.textContent="";


    } catch(erro){
        elStatus.textContent="Nao foi possivel medir a velocidade. Tente novamente";
        console.error(erro);
    } finally{
        botao.disabled=false;
        botao.textContent="Start Test";
    }
}
botao.addEventListener("click", rodarteste);