# io.swagger.client - Kotlin client library for FastAPI

## Requires

* Kotlin 1.4.30
* Gradle 5.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in Swagger definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**createDashboardDashboardsPost**](docs/DefaultApi.md#createdashboarddashboardspost) | **POST** /dashboards | Create Dashboard
*DefaultApi* | [**createEntryEntriesPost**](docs/DefaultApi.md#createentryentriespost) | **POST** /entries | Create Entry
*DefaultApi* | [**newSeriesSeriesPost**](docs/DefaultApi.md#newseriesseriespost) | **POST** /series | New Series

<a name="documentation-for-models"></a>
## Documentation for Models

 - [io.swagger.client.models.AnyOfValidationErrorLocItems](docs/AnyOfValidationErrorLocItems.md)
 - [io.swagger.client.models.CreateDashboard](docs/CreateDashboard.md)
 - [io.swagger.client.models.CreateEntry](docs/CreateEntry.md)
 - [io.swagger.client.models.CreateSeries](docs/CreateSeries.md)
 - [io.swagger.client.models.HTTPValidationError](docs/HTTPValidationError.md)
 - [io.swagger.client.models.ValidationError](docs/ValidationError.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
