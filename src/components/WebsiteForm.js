const WebsiteForm = () => {
    return (
        <form className={"WebsiteForm"}>
            <input type={"text"} placeholder={"Your URL"} name={"url"}/>
            <input type={"text"} placeholder={"Shortly about project"} name={"comment"}/>
            <button>Analyze</button>
        </form>
    );
}

export default WebsiteForm;
