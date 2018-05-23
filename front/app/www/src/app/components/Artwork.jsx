import React     from 'react'
import { Link }  from 'react-router-dom'


class ArtworkItem extends React.Component {
    constructor(props) {
        super(props)
        console.log(this.props.match.params.id)
        this.state = {
            liked: false
        }
        fetch(`http://pitipoulpe.freeboxos.fr/api/artworks/${this.props.match.params.id}/` )
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
    }

    like(id) {
        console.log('like '+ id)
    }

    render() {
        return (
            <div>Hello Artwork</div>
        )
    }
}

export default ArtworkItem