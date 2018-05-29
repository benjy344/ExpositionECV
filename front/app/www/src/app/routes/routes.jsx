import App from "../components/App";
import About from "../components/About";
import {history} from "../generalStore/Store";
import Artwork from "../components/Artwork";
import ConnectedRouter from "react-router-redux/es/ConnectedRouter";
import Nav from "../components/Nav";
import {Route} from "react-router";

const routes = ({}) =>
    <ConnectedRouter history={history}>
        <div>
            <Nav />
            <Route exact path="/" component={App}/>
            <Route path="/about" component={About}/>
            <Route path="/artwork/:id" component={Artwork}/>
        </div>
    </ConnectedRouter>

export default routes