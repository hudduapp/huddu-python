# DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDashboardDashboardsPost**](DefaultApi.md#createDashboardDashboardsPost) | **POST** /dashboards | Create Dashboard
[**createEntryEntriesPost**](DefaultApi.md#createEntryEntriesPost) | **POST** /entries | Create Entry
[**newSeriesSeriesPost**](DefaultApi.md#newSeriesSeriesPost) | **POST** /series | New Series

<a name="createDashboardDashboardsPost"></a>
# **createDashboardDashboardsPost**
> Object createDashboardDashboardsPost(body)

Create Dashboard

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
CreateDashboard body = new CreateDashboard(); // CreateDashboard | 
try {
    Object result = apiInstance.createDashboardDashboardsPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#createDashboardDashboardsPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboard**](CreateDashboard.md)|  |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createEntryEntriesPost"></a>
# **createEntryEntriesPost**
> Object createEntryEntriesPost(body)

Create Entry

creates a new entry to a series if it exists &amp; the request contains a valid token   :param request: :param data: :return:

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
CreateEntry body = new CreateEntry(); // CreateEntry | 
try {
    Object result = apiInstance.createEntryEntriesPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#createEntryEntriesPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntry**](CreateEntry.md)|  |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="newSeriesSeriesPost"></a>
# **newSeriesSeriesPost**
> Object newSeriesSeriesPost(body)

New Series

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
CreateSeries body = new CreateSeries(); // CreateSeries | 
try {
    Object result = apiInstance.newSeriesSeriesPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#newSeriesSeriesPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSeries**](CreateSeries.md)|  |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

