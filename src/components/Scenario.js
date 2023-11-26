import {useScenario} from "../provider/ScenarioProvider";

const Scenario = () => {
    const {title, img, problems, position, pros, cons} = useScenario();

    const prosList = pros.map((item, index) => {
        return <li key={index}>{item}</li>
    })
    const consList = cons.map((item, index) => {
        return <li key={index}>{item}</li>
    })

    return(
        <div className={"Scenario"}>
            <div>
                <button>Back</button>
                <img src={img} alt={""}/>
            </div>
            <div>
                <div>
                <h3>What is good:</h3>
                    <ul>{prosList}</ul>
                </div>
                <div>
                    <h3>What can be better:</h3>
                    <ul>{consList}</ul>
                </div>
            </div>
        </div>
    )
}

export default Scenario