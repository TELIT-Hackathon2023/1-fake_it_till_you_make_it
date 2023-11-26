import warningIcon from "../assets/images/warning.svg"

const ScenarioCard = ({title, img, problems, position}) => {
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
            <button>See details</button>
        </div>
    )
}

export default ScenarioCard;