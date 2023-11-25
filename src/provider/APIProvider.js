import {createContext, useContext, useState} from "react";

const APIContext = createContext(undefined);

const APIProvider = ({children}) => {
    const [api, setApi] = useState("http://192.168.142.173:8000/");

    return <APIContext.Provider value={api}>
            {children}
        </APIContext.Provider>
}

export const useAPI = () => useContext(APIContext);

export default APIProvider;