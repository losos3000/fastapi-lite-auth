import axios from "axios";

import clientConfig from '../../../configurations/clientConfig.json'



const baseConfig = () => {
    const c = clientConfig.axios
    const _protocol = c.useHttps ? "https" : "http"
    const _address = c.useHttps ? `${c.serverDomain}` : `${c.serverHost}:${c.serverPort}`

    console.log(`${_protocol}://${_address}/${c.apiPrefix}`)

    return {
        baseURL: `${_protocol}://${_address}/${c.apiPrefix}`,
        timeout: c.timeout,
        headers: c.headers,
        withCredentials: c.withCredentials,
        method: c.defaultMethod,
        credentials: 'include',
    }
}


export const apiGet = async (url: string = "/", config: object = {}) => {
    return await axios({
        ...baseConfig(),
        ...config,
        method: "get",
        url: url,
    })
}


export const apiPost = async (url: string = "/", body: object = {}, config: object = {}) => {
    return await axios({
        ...baseConfig(),
        ...config,
        method: "post",
        url: url,
        data: JSON.stringify(body),
    })
}