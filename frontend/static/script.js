async function buscar() {
  const trecho = document.getElementById("trecho").value.trim();
  const resultadosDiv = document.getElementById("resultados");
  resultadosDiv.innerHTML = "🔎 Buscando...";

  const resposta = await fetch("/buscar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ trecho: trecho })
  });

  const dados = await resposta.json();

  if (dados.length === 0) {
    resultadosDiv.innerHTML = "❌ Nenhuma música encontrada.";
    return;
  }

  resultadosDiv.innerHTML = "";
  dados.forEach(item => {
    const bloco = document.createElement("div");
    bloco.innerHTML = `<h3>🎤 ${item.musica}</h3>`;

    item.trechos.forEach(trecho => {
    const p = document.createElement("p");
    p.innerHTML = `➜ <a href="/musica/${item.arquivo}">${trecho}</a>`;
    // nome do arquivo: já salvo com "_" no lugar de espaços
    const nomeArquivo = item.musica.toLowerCase().replace(/ /g, "_");
    bloco.appendChild(p);
  });

    resultadosDiv.appendChild(bloco);
  });
}

// Limpa o campo de busca e os resultados
async function limpar() {
  document.getElementById("trecho").value = "";
  document.getElementById("resultados").innerHTML = "";
}

// Busca ao pressionar Enter
document.getElementById("trecho").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // impede recarregar a página
        buscar(); // chama a função de busca
    }
});