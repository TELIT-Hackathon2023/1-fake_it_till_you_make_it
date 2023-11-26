import {createContext, useContext, useState} from "react";

const ScenarioContext = createContext(undefined);
const ChangeScenarioContext = createContext(undefined);

const ScenarioProvider = ({children}) => {
    const [scenario, setScenario] = useState({});

    return <ChangeScenarioContext.Provider value={setScenario}>
        <ScenarioContext.Provider value={scenario}>
            {children}
        </ScenarioContext.Provider>
    </ChangeScenarioContext.Provider>
}

export const useScenario = () => useContext(ScenarioContext);
export const useChangeScenario = () => useContext(ChangeScenarioContext);

export default ScenarioProvider