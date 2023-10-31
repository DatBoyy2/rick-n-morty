                var offset = 20;  // Número de personajes ya cargados inicialmente

                document.getElementById('load-more-button').addEventListener('click', function() {
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', '/load-more-characters?offset=' + offset, true);
                    xhr.onload = function() {
                        if (xhr.status >= 200 && xhr.status < 400) {
                            var newCharacters = JSON.parse(xhr.responseText);
                            var cardContainer = document.querySelector('.card-container');
                            newCharacters.forEach(function(character) {
                                var card = document.createElement('div');
                                card.className = 'card';
                                card.innerHTML = `

                                    <a href="/character/${character.id}">
                                        <div class="card-inner">
                                            <div class="card-front">
                                                <img class="card-image" src="${character.image}" alt="${character.name}">
                                            </div>
                                            <div class="card-back">
                                                <p>${character.name}</p>
                                                <p>Status: ${character.status}</p>
                                                <p>Species: ${character.species}</p>
                                                <p>Gender: ${character.gender}</p>
                                            </div>
                                        </div>
                                    </a>
                                `;
                                cardContainer.appendChild(card);
                            });
                            offset += newCharacters.length;  // Actualizar el offset para la próxima carga
                        } else {
                            console.error('Error al cargar más personajes');
                        }
                    };
                    xhr.send();
                });