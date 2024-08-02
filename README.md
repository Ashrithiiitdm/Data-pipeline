  <h1 align="center">Data-pipeline</h1>
  
## Introduction

This repository contains a custom ELT project that involves utilization of Docker and postgresql alongside with dbt for changing the persistent data.
Extract - Data from a source database is extracted and is converted into a dump file.
Load - The file is then loaded into a destination database using a Python script.
Transform - The database can be transformed accordingly to our use.
