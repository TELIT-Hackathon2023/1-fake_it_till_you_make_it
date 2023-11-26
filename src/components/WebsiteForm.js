import {useNavigate} from "react-router-dom";
import {useSetUrl} from "../provider/URLProvider";
import {useState} from "react";

const WebsiteForm = () => {
    const navigate = useNavigate();
    const setUrl = useSetUrl();
    const [inputs, setInputs] = useState({
        url: "",
        gitUrl: "",
        comment: ""
    });

    const submitHandler = () => {
        setUrl(inputs.url);
        navigate("/scenarios");
    }

    const inputHandler = (e, input) => {
        setInputs(prevState => ({
            ...prevState,
            [input]: e.target.value
        }));
    };

    return (
            <form className={"WebsiteForm"} onSubmit={submitHandler}>
                <h1>Start testing your website</h1>
                <input onChange={(e) => inputHandler(e, "url")}
                       value={inputs.url}
                       type={"text"}
                       placeholder={"URL-address your website"}
                       name={"url"}
                       required={true}/>
                <input onChange={(e) => inputHandler(e, "gitUrl")}
                       value={inputs.gitUrl}
                       type={"text"}
                       placeholder={"URL-address your website (optional)"}
                       name={"url"}/>
                <div className={"add-files"}><button>+ Add files</button></div>
                <textarea onChange={(e) => inputHandler(e, "comment")}
                          value={inputs.comment}
                          rows={5}
                          placeholder={"Shortly about project"}
                          name={"comment"}
                          required={true}/>
                <div className={"start"}>
                    <button>START</button>
                </div>
            </form>
    );
}

export default WebsiteForm;
