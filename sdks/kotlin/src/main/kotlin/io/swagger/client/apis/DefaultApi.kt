/**
 * FastAPI
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.apis

import io.swagger.client.models.CreateDashboard
import io.swagger.client.models.CreateEntry
import io.swagger.client.models.CreateSeries
import io.swagger.client.models.HTTPValidationError

import io.swagger.client.infrastructure.*

class DefaultApi(basePath: kotlin.String = "/") : ApiClient(basePath) {

    /**
     * Create Dashboard
     * 
     * @param body  
     * @return kotlin.Any
     */
    @Suppress("UNCHECKED_CAST")
    fun createDashboardDashboardsPost(body: CreateDashboard): kotlin.Any {
        val localVariableBody: kotlin.Any? = body
        
        val localVariableConfig = RequestConfig(
                RequestMethod.POST,
                "/dashboards"
        )
        val response = request<kotlin.Any>(
                localVariableConfig, localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as kotlin.Any
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
    /**
     * Create Entry
     * creates a new entry to a series if it exists &amp; the request contains a valid token   :param request: :param data: :return:
     * @param body  
     * @return kotlin.Any
     */
    @Suppress("UNCHECKED_CAST")
    fun createEntryEntriesPost(body: CreateEntry): kotlin.Any {
        val localVariableBody: kotlin.Any? = body
        
        val localVariableConfig = RequestConfig(
                RequestMethod.POST,
                "/entries"
        )
        val response = request<kotlin.Any>(
                localVariableConfig, localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as kotlin.Any
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
    /**
     * New Series
     * 
     * @param body  
     * @return kotlin.Any
     */
    @Suppress("UNCHECKED_CAST")
    fun newSeriesSeriesPost(body: CreateSeries): kotlin.Any {
        val localVariableBody: kotlin.Any? = body
        
        val localVariableConfig = RequestConfig(
                RequestMethod.POST,
                "/series"
        )
        val response = request<kotlin.Any>(
                localVariableConfig, localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as kotlin.Any
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
}
