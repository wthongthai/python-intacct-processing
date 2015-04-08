# python-intacct-processing

This script was written to process an intacct (timelog) report to combine Coding and QA time from questions of the same type to get true "coding touch time".  
<em>Note: The script was not designed to work with headers, which were added here for clarity.</em>

<h2>For example</h2>
<h4>Input</h4>
<table>
  <tr>
    <th>Project</th><th>Task</th><th>Time (hrs)</th><th>#</th>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - B</td><td>2</td><td>3</td>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - MI</td><td>4</td><td>2</td>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - BSMI</td><td>2.75</td><td>1</td>
  </tr>
  <tr>
    <td>Project A</td><td>QA - B</td><td>1</td><td>3</td>
  </tr>
  <tr>
    <td>Project A</td><td>QA - BSMI</td><td>1.25</td><td>2</td>
  </tr>
  <tr>
    <td>Project B</td><td>Coding - B</td><td>10</td><td>8</td>
  </tr>
  <tr>
    <td>Project B</td><td>Coding - MI</td><td>4</td><td>2</td>
  </tr>
  <tr>
    <td>Project B</td><td>QA - B</td><td>2</td><td>6</td>
  </tr>
</table>

<h4>Output</h4>
<table>
  <tr>
    <th>Project</th><th>Task</th><th>Time (hrs)</th><th>#</th>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - B</td><td>3</td><td>3</td>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - MI</td><td>4</td><td>2</td>
  </tr>
  <tr>
    <td>Project A</td><td>Coding - BSMI</td><td>4</td><td>1</td>
  </tr>
  <tr>
    <td>Project A</td><td>QA - B</td><td>1</td><td>3</td>
  </tr>
  <tr>
    <td>Project A</td><td>QA - BSMI</td><td>1.25</td><td>2</td>
  </tr>
  <tr>
    <td>Project B</td><td>Coding - B</td><td>12</td><td>8</td>
  </tr>
  <tr>
    <td>Project B</td><td>Coding - MI</td><td>4</td><td>2</td>
  </tr>
  <tr>
    <td>Project B</td><td>QA - B</td><td>2</td><td>6</td>
  </tr>
</table>
