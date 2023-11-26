import {useAPI} from "../provider/APIProvider";
import React, {useEffect, useState} from "react";
import {useUrl} from "../provider/URLProvider";
import ScenarioCard from "./ScenarioCard";
import arrow_up from "../assets/images/arrow_up.svg"
import arrow_down from "../assets/images/arrow_down.svg"
import line from "../assets/images/line.svg"
import Scores from "./Scores";

const ScenariosPage = () => {
    const API = useAPI();
    const url = useUrl();

    const [loading, setLoading] = useState(true);
    const [scenarios, setScenarios] = useState([]);

    useEffect(() => {
        const fetchScenarios = async () => {
            try {
                console.log(API + "chat/?url=" + url);
                const response = await fetch(API + "chat/?url=" + url);

                if (!response.ok) {
                    throw new Error('No data');
                }

                const result = await response.json();
                setScenarios(result);
            } catch (e) {
                console.log(e);
            } finally {
                setLoading(false);
            }
        }

        fetchScenarios();
    }, [])

    const scenariosCards = scenarios.map((scenario, index) => {
        return <>
            {index % 2
                ? <>
                    {(scenarios.length !== index - 1 && index !== 0) && <img src={arrow_down} alt={""}/>}
                    <ScenarioCard
                        key={index}
                        title={scenario.title}
                        img={scenario.img}
                        problems={scenario.problems}
                        pros={scenario.pros}
                        cons={scenario.cons}
                        position={true}
                    />
                </>
                : <>
                    {(scenarios.length !== index - 1 && index !== 0) && <img src={arrow_up} alt={""}/>}
                    <ScenarioCard
                        key={index}
                        title={scenario.title}
                        img={scenario.img}
                        problems={scenario.problems}
                        pros={scenario.pros}
                        cons={scenario.cons}
                        position={false}
                    />
                </>
            }
        </>
    });

    return (
        <div className={"ScenariosPage"}>
            {loading
                ? <p>Loading...</p>
                : <>
                    <div className={"scenario-info"}>
                        <img src={line} alt={""}/>
                        <p>The user lands on the homepage, where they're greeted with a variety of deals, prominently
                            including the 'Black Friday' specials. Browsing through the categories, they are drawn to
                            the toys section, where they find a LEGO DUPLO Box set on offer. Intrigued by the set, they
                            review the product details, check the price, and decide to add it to their shopping cart.
                            With the LEGO set in the cart, they proceed to checkout, ready to finalize their
                            purchase. </p>
                    </div>
                    <div className={"scenariosCards"}>{scenariosCards}</div>
                    <Scores/>
                </>
            }
        </div>
    )
}

export default ScenariosPage