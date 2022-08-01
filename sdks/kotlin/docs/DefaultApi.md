# DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDashboardDashboardsPost**](DefaultApi.md#createDashboardDashboardsPost) | **POST** /dashboards | Create Dashboard
[**createEntryEntriesPost**](DefaultApi.md#createEntryEntriesPost) | **POST** /entries | Create Entry
[**newSeriesSeriesPost**](DefaultApi.md#newSeriesSeriesPost) | **POST** /series | New Series

<a name="createDashboardDashboardsPost"></a>
# **createDashboardDashboardsPost**
> kotlin.Any createDashboardDashboardsPost(body)

Create Dashboard

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = DefaultApi()
val body : CreateDashboard =  // CreateDashboard | 
try {
    val result : kotlin.Any = apiInstance.createDashboardDashboardsPost(body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#createDashboardDashboardsPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#createDashboardDashboardsPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboard**](CreateDashboard.md)|  |

### Return type

**kotlin.Any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createEntryEntriesPost"></a>
# **createEntryEntriesPost**
> kotlin.Any createEntryEntriesPost(body)

Create Entry

creates a new entry to a series if it exists &amp; the request contains a valid token   :param request: :param data: :return:

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = DefaultApi()
val body : CreateEntry =  // CreateEntry | 
try {
    val result : kotlin.Any = apiInstance.createEntryEntriesPost(body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#createEntryEntriesPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#createEntryEntriesPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntry**](CreateEntry.md)|  |

### Return type

**kotlin.Any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="newSeriesSeriesPost"></a>
# **newSeriesSeriesPost**
> kotlin.Any newSeriesSeriesPost(body)

New Series

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = DefaultApi()
val body : CreateSeries =  // CreateSeries | 
try {
    val result : kotlin.Any = apiInstance.newSeriesSeriesPost(body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#newSeriesSeriesPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#newSeriesSeriesPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSeries**](CreateSeries.md)|  |

### Return type

**kotlin.Any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

