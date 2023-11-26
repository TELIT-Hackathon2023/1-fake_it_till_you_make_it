import './App.css';
import ScenariosPage from "./components/ScenariosPage";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import APIProvider from "./provider/APIProvider";
import URLProvider from "./provider/URLProvider";
import Background from "./components/Background";
import WebsiteForm from "./components/WebsiteForm";

function App() {
    return (
        <APIProvider>
            <URLProvider>
                <div className={"App"}>
                    <BrowserRouter>
                        <Background>
                            <Routes>
                                <Route path={"/"} element={<WebsiteForm/>}/>
                                <Route path={"/scenarios"} element={<ScenariosPage/>}/>
                            </Routes>
                        </Background>
                    </BrowserRouter>
                </div>
            </URLProvider>
        </APIProvider>
    );
}

export default App;
