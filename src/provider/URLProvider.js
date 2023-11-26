import React, { createContext, useContext, useState } from "react";

const URLContext = createContext(undefined);
const ChangeURLContext = createContext(undefined);

const URLProvider = ({ children }) => {
    const [url, setUrl] = useState("https://www.alza.sk/");

    return (
        <ChangeURLContext.Provider value={setUrl}>
            <URLContext.Provider value={url}>
                {children}
            </URLContext.Provider>
        </ChangeURLContext.Provider>
    );
};

export const useUrl = () => useContext(URLContext);
export const useSetUrl = () => useContext(ChangeURLContext);

export default URLProvider;
