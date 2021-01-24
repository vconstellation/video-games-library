console.log('hello')

const gamesBox = document.getElementById('games-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')




let visible = 8

const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/games/list/${visible}`,
        success: function(res) {
            const data = res.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                data.map(game=>{
                    console.log(game.id)
                    gamesBox.innerHTML += `<div class="card">
                                                ${game.name}
                                                <br>
                                                <img src="media/${game.cover}">
                                            </div>`
                })
            }, 500)
            max_size = res.max
            
            if(max_size) {
                console.log('done')
            }
        },
        error: function(err) {
            console.log(err)
        }
    })
}

handleGetData()

loadBtn.addEventListener('click', () => {
    visible += 8
    handleGetData()
})