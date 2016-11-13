$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

$(function() {
  var Aladdin = new blk.API();
  Aladdin.portfolioAnalysis({
    positions: 'GVPIX~4.77|MGLMX~32.99|RCWCX~20.14|CLNCX~28.92|GGIAX~13.18|',
    filter: 'countryCode:US'
  }, function(data) {
    var portfolio = data.resultMap.PORTFOLIOS[0].portfolios[0];
    $('#holdings').DataTable({
      data: portfolio.holdings.map(function(holding) {
        return [holding.ticker, holding.description, holding.assetType, holding.weight]
      }),
      columns: [{
        title: 'Ticker'
      }, {
        title: 'Description'
      }, {
        title: 'Asset Type'
      }, {
        title: 'Weight'
      }, {
          title: 'Tone'
      }],
      order: [
        [0, 'desc']
      ]
    });
    $('#returns').highcharts('StockChart', {
      rangeSelector: {
        selected: 5
      },
      series: [{
        name: 'Portfolio',
        data: portfolio.returns.performanceChart.map(function(point) {
          return [point[0], point[1] * 10000]
        }),
        tooltip: {
          valueDecimals: 2
        }
      }]
    });

  });
});