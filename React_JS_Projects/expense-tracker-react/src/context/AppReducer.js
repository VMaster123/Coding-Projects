export default(state,action) => {

    switch(action.type) {
        default:
            return state;
        case 'DELETE-TRANSACTION':
            return {
                ...state,
                transactions: state.transactions.filter(transaction => transaction.id !== action.payload)

            }
        case 'ADD-TRANSACTION':
            return {
                ...state,
                transactions: [action.payload,...state.transactions]

            }
            


    }
}