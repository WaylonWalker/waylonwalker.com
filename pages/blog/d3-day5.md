---
templateKey: 'blog-post'
title: D3 Day 5
slug: d3-day-5
date: 2018-05-08
category: Viz
tags:
    - webdev
status: draft
summary: Today we are adding Axes to the horizontal bar chart that we have worked on throughout the past few days.
description: none
cover: "./d3-cropped.png"
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/4.13.0/d3.min.js'></script>
<style>
    #content{
        max-width: 800px;
        margin: 0 auto;
    }
    .chart {
        display: block;
        padding: 10px;
        background: peachpuff;
    }

    .bar {
        height: 30px;
        margin: 5px;
        background: teal;
    }
    .bar:hover{
        background: #444;
        }
    button {
        background: rgb(240, 196, 211);
        border: none;
        font-size: 1.3rem;
        border-radius: 5px;
        padding: .2rem 1rem;
        margin-bottom: 1rem
    }
    .on {
        background: palevioletred;
    }
    .big {
    width: 100%
    }
    .small {
    width: 50%
    }
</style>


## Learn D3 in 5 days

For what we are creating in these posts d3 is way overkill and very verbose, but I need to start somewhere!  These are just stepping stones into real custom visualizations that cannot be done in any other tool today.  I still cannot explain how excited I am to say **"I created that in d3!!!"**
### Todays Result

## Recall Example 3 from yesterday

<div id='buttons'>
    <h3>Subject</h3>
    <div id='subjects'>
        <button class='math' onclick="render4('math')">Math</button>
        <button class='science' onclick="render4('science')">Science</button>
    </div>
    <h3>Chart Size</h3>
    <div id='sizes'>
        <button class='chart4-big-btn' onclick='chart4_size("big")')>Large</button>
        <button class='chart4-small-btn' onclick='chart4_size("small")'>Small</button>
    </div>
</div>

<div id="chart4" class='chart'></div>



<script>
    const data4 = [
        { name: 'Alice', math: 93, science: 84},
        { name: 'Bob', math: 73, science: 82 },
        { name: 'James', math: 92, science: 78},
        { name: 'Steve', math: 77, science: 93 },
        { name: 'Jordan', math: 80, science: 68 },
    ]

    chart4 = document.getElementById('chart4')


    let width = function() {
        return chart4.getBoundingClientRect().width
        }
    let height = function() {
        return chart4.getBoundingClientRect().height
        }
    let barHeight = function() {
        height() /  data4.length + 'px'
        }

    function chart4_size(size) {
        d3.select('#sizes')
            .selectAll('button')
            .classed('on', false)
        d3.select('#sizes')
            .select('.chart4-' + size + '-btn')
            .classed('on', true)
        d3.select('#chart4')
            .attr('class', 'chart ' + size)
        subject = document
            .getElementById('subjects')
            .querySelector('.on')
            .classList[0]
        render4(subject)
    }

    function render4(subject) {

        d3.select('#subjects')
            .selectAll('button')
            .classed('on', false);

        d3.select('#subjects')
            .select('.' + subject)
            .attr('class', subject + ' on');

        let xScale = d3.scaleLinear()
            .domain([50, 100])
            .range([0, width()]);

        const bars5 = d3.select('#chart4')
            .selectAll('div')
            .data(data4, function(d) {
                return d.name
            })
        const newBars = bars5.enter()
            .append('div')
                .attr('class', 'bar')
                .style('width', 0)

        newBars.merge(bars5)
            .transition()
            .style('width', function(d) {
                return xScale(d[subject]) + 'px'
            })
            .style('height', barHeight())
    }
    render4('math')
    chart4_size('big')
</script>


## Final Result

<div id='buttons5'>
    <h3>Subject</h3>
    <div id='subjects5'>
        <button class='math' onclick="render5('math')">Math</button>
        <button class='science' onclick="render5('science')">Science</button>
    </div>
    <h3>Chart Size</h3>
    <div id='sizes5'>
        <button class='chart5-big-btn' onclick='chart5_size("big")')>Large</button>
        <button class='chart5-small-btn' onclick='chart5_size("small")'>Small</button>
    </div>
</div>

<div id="chart5" class='chart'></div>



<script>
    const data5 = [
        { name: 'Alice', math: 93, science: 84},
        { name: 'Bob', math: 73, science: 82 },
        { name: 'James', math: 92, science: 78},
        { name: 'Steve', math: 77, science: 93 },
        { name: 'Jordan', math: 80, science: 68 },
    ]

    chart5 = document.getElementById('chart5')


    let width5 = function() {
        return chart5.getBoundingClientRect().width
        }
    let height5 = function() {
        return chart5.getBoundingClientRect().height
        }
    let barHeight5 = function() {
        height5() /  data5.length + 'px'
        }


    function chart5_size(size) {
        d3.select('#sizes5')
            .selectAll('button')
            .classed('on', false)
        d3.select('#sizes5')
            .select('.chart5-' + size + '-btn')
            .classed('on', true)
        d3.select('#chart5')
            .attr('class', 'chart ' + size)
        subject = document
            .getElementById('subjects5')
            .querySelector('.on')
            .classList[0]
        console.log(subject)
        render5(subject)
    }

    function render5(subject) {

        d3.select('#subjects5')
            .selectAll('button')
            .classed('on', false);

        d3.select('#subjects5')
            .select('.' + subject)
            .attr('class', subject + ' on');

        let xScale = d3
            .scaleLinear()
            .domain([50, 100])
            .range([0, width5()]);


        const bars5 = d3.select('#chart5')
            .selectAll('div')
            .data(data5, function(d) {
                return d.name
            })
        const newBars = bars5
            .enter()
            .append('div')
                .attr('class', 'bar')
                .style('width', 0)

        newBars.merge(bars5)
            .transition()
            .style('width', function(d) {
                return xScale(d[subject]) + 'px'
            })
            .style('height', barHeight5())

        d3
         .select('#chart5')
         .select('svg')
         .remove()

        const svg5 = d3
            .select('#chart5')
            .append('svg')
            .attr('width', width5())
            .attr('height', height5())
            .style('position', 'relative')
            .append('g')
            .call(d3.axisBottom(xScale))
    }
    render5('math')
    chart5_size('big')
</script>
