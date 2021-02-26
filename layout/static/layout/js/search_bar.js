
const user_input = $("#user-input")
const endpoint = $("#search-box").attr("data-url");
const delay_by_in_ms = 0
let scheduled_function = false

const content_div = document.getElementById('content-box')
const input = document.getElementById('search-box')



const ajax_search = (endpoint, request_parameters) => {
    $.getJSON(endpoint, request_parameters).done((response) => {
        const content = response['html_from_view']
        content_div.innerHTML = content
    })
}

input.addEventListener('keyup', () => {
    content_div.innerHTML = " "
    const request_parameters = {
        q: input.value
    }
    if (request_parameters.q.length > 0) {
        setTimeout(() => {
            ajax_search(endpoint, request_parameters)
        }, 100)
    }
})
