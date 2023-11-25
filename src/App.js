import './App.css';
import ScenariosPage from "./components/ScenariosPage";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import APIProvider from "./provider/APIProvider";
import URLProvider from "./provider/URLProvider";
import EnteryPage from "./components/EnteryPage";

function App() {
    return (
        <APIProvider>
            <URLProvider>
                <div className={"App"}>
                    <BrowserRouter>
                        <Routes>
                            <Route path={"/"} element={<EnteryPage/>}/>
                            <Route path={"/scenarios"} element={<ScenariosPage/>}/>
                        </Routes>
                    </BrowserRouter>
                </div>
            </URLProvider>
        </APIProvider>
    );
}

export default App;
