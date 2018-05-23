import React from 'react'

import '../scss/main'
import ArtworkItem from "./ArtworkItem";

class App extends React.Component {

    constructor(props) {
        super(props)
        //const id = 1
        this.state = {
            errorMessage: null,
            content: null,
            artworks: []
        }
        fetch(`http://pitipoulpe.freeboxos.fr/api/places/1/pages/home` )
            .then( (response) => {
                console.log(response)
                if(!response.ok){
                    this.setState({
                        errorMessage:response.statusText
                    })
                } else {
                    response.json()
                        .then(resp => {
                            console.log(resp)
                            const content = resp.results[0].text
                            this.setState({
                                content
                            })
                        })
                }
            })
            .catch(err => console.log("Error: ", err))
        fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/` )
            .then( (response) => {
                console.log(response)
                if(!response.ok){
                    this.setState({
                        errorMessage:response.statusText
                    })
                } else {
                    response.json()
                        .then(resp => {
                            console.log(resp)
                            const artworks = resp.results
                            this.setState({
                                artworks
                            })
                        })
                }
            })
            .catch(err => console.log("Error: ", err))
    }

    createMarkup(content) {
        return {__html: content }
    }

    render() {
        return(
            <div>
                {this.state.errorMessage &&
                <span>{this.state.errorMessage}</span>
                }
                {this.state.content &&
                <div dangerouslySetInnerHTML={this.createMarkup(this.state.content)} ></div>
                }
                {this.state.artworks && this.state.artworks.length &&
                <ul>
                    {this.state.artworks.map((data, index) => (
                        <ArtworkItem key={index} id={index} artwork={data}/>
                    ))}
                </ul>
                }
            </div>
        )
    }
}

export default App