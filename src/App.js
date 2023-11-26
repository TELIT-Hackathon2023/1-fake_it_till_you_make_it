import './App.css';
import ScenariosPage from "./components/ScenariosPage";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import APIProvider from "./provider/APIProvider";
import URLProvider from "./provider/URLProvider";
import Background from "./components/Background";
import WebsiteForm from "./components/WebsiteForm";
import ScenarioProvider from "./provider/ScenarioProvider";
import Scenario from "./components/Scenario";

function App() {
    return (
        <ScenarioProvider>
            <APIProvider>
                <URLProvider>
                    <div className={"App"}>
                        <BrowserRouter>
                            <Background>
                                <Routes>
                                    <Route path={"/"} element={<WebsiteForm/>}/>
                                    <Route path={"/scenarios"} element={<ScenariosPage/>}/>
                                    <Route path={"/scenario"} element={<Scenario/>}/>
                                </Routes>
                            </Background>
                        </BrowserRouter>
                    </div>
                </URLProvider>
            </APIProvider>
        </ScenarioProvider>
    );
}

export default App;
