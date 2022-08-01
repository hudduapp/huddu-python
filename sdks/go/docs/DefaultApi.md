# {{classname}}

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDashboardDashboardsPost**](DefaultApi.md#CreateDashboardDashboardsPost) | **Post** /dashboards | Create Dashboard
[**CreateEntryEntriesPost**](DefaultApi.md#CreateEntryEntriesPost) | **Post** /entries | Create Entry
[**NewSeriesSeriesPost**](DefaultApi.md#NewSeriesSeriesPost) | **Post** /series | New Series

# **CreateDashboardDashboardsPost**
> Object CreateDashboardDashboardsPost(ctx, body)
Create Dashboard

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateDashboard**](CreateDashboard.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateEntryEntriesPost**
> Object CreateEntryEntriesPost(ctx, body)
Create Entry

creates a new entry to a series if it exists & the request contains a valid token   :param request: :param data: :return:

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateEntry**](CreateEntry.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **NewSeriesSeriesPost**
> Object NewSeriesSeriesPost(ctx, body)
New Series

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateSeries**](CreateSeries.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

