const WebsiteForm = () => {
    return (
        <form>
            <input type={"text"} placeholder={"Your URL"} name={"url"}/>
            <input type={"text"} placeholder={"Enter the action you want app to preform"} name={"comment"}/>
        </form>
    );
}

export default WebsiteForm;
