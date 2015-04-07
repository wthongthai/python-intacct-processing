# python-intacct-processing

This script was written to process an intacct (timelog) report to combine Coding and QA time from questions of the same type to get true "coding touch time".

<h2>For example</h2>
<h4>Original Data</h4>
<table>
  <tr>
    <td>Coding - B</td><td>2 hrs</td>
  </tr>
  <tr>
    <td>Coding - BSMI</td><td>4.5 hrs</td>
  </tr>
  <tr>
    <td>QA - B</td><td>1 hrs</td>
  </tr>
  <tr>
    <td>QA - BSMI</td><td>2.25 hrs</td>
  </tr>
</table>

<h4>Processed Data</h4>
<table>
  <tr>
    <td>Coding - B</td><td>3 hrs</td>
  </tr>
  <tr>
    <td>Coding - BSMI</td><td>6.75 hrs</td>
  </tr>
  <tr>
    <td>QA - B</td><td>1 hrs</td>
  </tr>
  <tr>
    <td>QA - BSMI</td><td>2.25 hrs</td>
  </tr>
</table>
