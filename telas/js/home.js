//adiciona a classe block no paragrafo que possui display none
var btnReadMore = document.getElementById('btn-read-more') 
btnReadMore.addEventListener('click', function() {
    //console.log("ola")
   var pReadMore = document.getElementById('p-read-more');
   //console.log(pReadMore);
   if(pReadMore.classList.contains('d-none'))
    {
        pReadMore.classList.remove('d-none')
        pReadMore.classList.add('d-block');
    } else
    {
        pReadMore.classList.remove('d-block')
        pReadMore.classList.add('d-none');
    }
});
//roda o scroll
var linksNav = document.querySelectorAll('.navbar-nav a');

linksNav.forEach(function(link) {
    link.addEventListener('click', function(event) {
    //    event.preventDefault();
        
        // pega texto dentro da tag <a> clicada
        var textoLink = link.textContent;
        if (textoLink.trim() === 'Contato') {
            var footer = document.getElementById('footerContato');
            var footerPosition = footer.offsetTop;
            
            // Rola até a posição do elemento
            window.scrollTo({
                top: footerPosition,
                behavior: 'smooth'
            });
        }
        if(textoLink.trim() ==='Sobre')
            {
                var aboutMore = document.getElementById('aboutMore');
                var aboutMorePosition = aboutMore.offsetTop;
                window.scrollTo({
                    top: aboutMorePosition,
                    behavior: 'smooth'
                });
            }
        if(textoLink.trim() === 'Home')
            {
                var header = document.getElementById('headerHome');
                var headerPosition = header.offsetTop;
                window.scrollTo({
                    top: headerPosition,
                    behavior: 'smooth'
                });
            }    
    });   
});
//fim roda scroll




