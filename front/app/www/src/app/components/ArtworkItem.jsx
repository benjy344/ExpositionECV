import React     from 'react'
import { Link }  from 'react-router-dom'


class ArtworkItem extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            liked: false
        }
    }

    like(id) {
        console.log('like '+ id)
    }

    render() {
        return (
            <li className={"artwork "}>
                <div className="artwork-image">
                    <Link to={`/artwork/${this.props.id}`}>
                        <img src={this.props.artwork.img} alt="placeholder" />
                    </Link>
                </div>
                <div className="product-details">
                    <h3><a href="#0">{this.props.artwork.name}</a></h3>
                    <div className="actions">
                        <button className="like-item" onClick={this.like.bind(this, this.props.id)}>like</button>
                    </div>
                </div>
            </li>
        )
    }
}

export default ArtworkItem