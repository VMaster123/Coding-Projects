import './App.css';
import Headers from './components/Headers';
import Balance from './components/Balance';
import IncomeExpenses from './components/IncomeExpenses';
import TransactionList from './components/TransactionList';
import AddTransaction from './components/AddTransaction';
import {GlobalProvider} from './context/GlobalState'


function App() {
  return (
    <GlobalProvider>
      <Headers />
      <div className = "container">
        <Balance />
        <IncomeExpenses />
        <TransactionList/>
        <AddTransaction />
      </div>
    </GlobalProvider>
  );
}

export default App;
