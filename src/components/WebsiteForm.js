import {useNavigate} from "react-router-dom";
import {useSetUrl} from "../provider/URLProvider";
import {useState} from "react";

const WebsiteForm = () => {
    const navigate = useNavigate();
    const setUrl = useSetUrl();
    const [urlInput, setUrlInput] = useState("");

    const submitHandler = () => {
        setUrl(urlInput);
        navigate("/scenarios");
    }

    const inputHandler = (e) => {
        setUrlInput(e.target.value);
    }

    return (
        <form className={"WebsiteForm"} onSubmit={submitHandler}>
            <h1>Start testing your website</h1>
            <input onChange={(e) => inputHandler(e)}
                   value={urlInput}
                   type={"text"}
                   placeholder={"Your URL"}
                   name={"url"}/>
            <textarea rows={5} placeholder={"Shortly about project"} name={"comment"}/>
            <button>Analyze</button>
        </form>
    );
}

export default WebsiteForm;
