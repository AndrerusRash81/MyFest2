
 class App extends React.Component {
     _mounted = true;
     loading  = false;
     hasError = false;

     constructor(props) {
        super(props)
        this.state = { bids: [] }
     }

     componentDidMount() {
       //при создании конструктора -инициализация
       this._mounted = true;
       this.fetchData();
     }

    componentWillUnmount() {
       //при выходе
       this._mounted = false;
    }

     fetchData() {
          console.log('fetching...');
          this.loading = true;
          fetch('/api/newsserializers/')
          .then(res => res.json())
          .then((data) => {
          if (this._mounted) {
              console.log('Загрузка данных таблицы...');
              console.log(data);
              this.setState({ bids: data }, function () { this.render(); });
              this.loading = false;
          } else {
             console.log('нет данных.');
          }
      })
      .catch(err => {
        this.hasError = true;
        this.loading  = false;
      })
     }

     renderTableData() {
        const bids = this.state.bids;
        console.log('Формирование данных таблицы...');
        console.log(bids.data);
        console.log(bids.length);
        if (bids.length > 0) {
         return bids.map((bid, index) => {
           bid.room = bid.room ? new Intl.NumberFormat('ru-RU', { minimumFractionDigits: 2 }).format(+bid.room) : '';
           bid.date = this.getFormattedDate(bid.date);
           return (
             <tr key={bid.id}>
               <td>{bid.title}</td>
               <td>{bid.date}</td>
               <td>{bid.avtor}</td>
               <td>{bid.room} </td>
             </tr>
           )
         });
       } else if (this._mounted) {
         return (<tr><td>Новостей нет</td></tr>);
       } else {
         return (<tr><td>Загрузка...</td></tr>);
       }
     }


     render() {
       return (
         <div className="table-container">
           {this.props.visible == 'True' && <h1>visible =True</h1>}
           <h1>This my table {this.props.nametable} комната {this.props.room} </h1>
                           <table  class="table_my_2">
                           <thead>
                           <tr scope = "name">
                            <th>Описание-</th>
                            <th>Дата-</th>
                            <th>Автор-</th>
                            <th>Комната-</th>
                            </tr>
                            </thead>
                           <tbody>
                              {this.renderTableData()}
                           </tbody>
                           </table>
         </div>
       );

     }

     pad(num, length) {
       if ((''+num).length >= length) return num;
       var lead = '0' + new Array(length).join('0')
       return (lead + num).slice(-length);
     }

     getFormattedDate(date) {
       const d = new Date(Date.parse(date));
       const day = this.pad(d.getDate(),2);
       const month = this.pad(d.getMonth()+1,2);
       const year = this.pad(d.getFullYear(),2);
       const hour = this.pad(d.getHours(),2);
       const minute = this.pad(d.getMinutes(),2);
       const second = this.pad(d.getSeconds(),2);
       const msec = this.pad(d.getMilliseconds(),3);
       return `${day}.${month}.${year} ${hour}:${minute}:${second}.${msec}`;
     }

 }
