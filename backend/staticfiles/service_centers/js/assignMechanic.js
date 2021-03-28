function assignMech(reqid) {
    
    let mechanic = document.getElementById(`req${reqid}`).value
    console.log(mechanic)
    let csrf = document.querySelector('input').value
    console.log(csrf)
    fetch('/mechanic/assign',{
        method :'POST',
        headers:{
            'X-CSRFToken' : csrf
        },
        body:JSON.stringify({reqid , mech_id : mechanic})
    })
    .then(data => data.json())
    .then(data => {console.log(data)})
    
    location.reload()
}