import { Fragment } from "react";
import { connect } from "react-redux";

import { CheckCircleIcon } from '@heroicons/react/solid';

function Alert ({ alert }) {

    const displayAlert = () => {
        if (alert !== null){
            return (
                <div className={`rounded-md ${alert.alertColor} p-4`}>
                    <div className="flex">
                        <div className="flex-shrink-0">
                        <CheckCircleIcon className={`h-5 w-5 text-gray-700`} aria-hidden="true" />
                        </div>
                        <div className="ml-3">
                        <p className={`text-sm font-medium text-gray-800`}>{alert.msg}</p>
                        </div>
                    </div>
                </div>
            )
        } else {
            return(
                <Fragment></Fragment>
            )
        }
    }

    return (
        <Fragment>
            {displayAlert()} 
        </Fragment>
    )
}

const mapStateToProps = state => ({
    alert: state.Alert.alert
})

export default connect(mapStateToProps)(Alert)