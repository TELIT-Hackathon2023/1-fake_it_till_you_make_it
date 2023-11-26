import warningIcon from "../assets/images/warning.svg"
import {useNavigate} from "react-router-dom";
import {useChangeScenario} from "../provider/ScenarioProvider";

const ScenarioCard = ({title, img, problems, position, pros, cons}) => {
    const navigate = useNavigate();
    const setScenario = useChangeScenario();

    const detailsHandler = () => {
        setScenario({title, img, problems, position, pros, cons});
        navigate("/scenario");
    }

    return (
        <div className={"ScenarioCard"}
             style={{marginTop: position ? '7rem' : 'none'}}
        >
            <h2>{title}</h2>
            <img className={"ScenarioCard-img"} src={img} alt={""}/>
            <div className={"warnings"}>
                <img src={warningIcon} alt={""}/>
                <p>{`Discovered ${problems} problems`}</p>
            </div>
            <button onClick={detailsHandler}>See details</button>
        </div>
    )
}

export default ScenarioCard;