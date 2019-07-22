import React from 'react';
import PropTypes from 'prop-types';
import { Modal, Navbar } from 'react-bulma-components/full'

class NavModal extends React.Component {
    static propTypes = {
        modal: PropTypes.object,
        name: PropTypes.string,
        children: PropTypes.node.isRequired,
    };

    static defaultProps = {
        modal: {}
    };
    
    state = {
        show: false,
    };

    open = () => {this.setState({ show: true })}
    close = () => {this.setState({ show: false})}

    render() {
        return (
            <>
            <Navbar.Item href="#" onClick={this.open}>{this.props.name}</Navbar.Item>
            <Modal show={this.state.show} onClose={this.close} {...this.props.modal}>
                {this.props.children}
            </Modal>
            </>
        );
    }
}

export default NavModal