import axios from "axios"

export {
    classifyDigit
}

async function request(urlSuffix, options, callback){
    await axios('http://localhost:5000/' + urlSuffix, options)
            .then((response) => { 
                console.log(response)
                callback(JSON.parse(JSON.stringify(response['data']))); 
            })
            .catch((error) => console.error("Error: ", error));
}

async function classifyDigit(options, callback){
    request("Digit", options, callback);
}