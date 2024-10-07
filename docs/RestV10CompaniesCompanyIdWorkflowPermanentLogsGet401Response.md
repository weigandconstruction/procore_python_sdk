# RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**fields** | **str** |  | [optional] 
**reason** | **str** | A human-readable code providing additional detail on the cause of the error. | [optional] 
**error** | **str** | Description of the error thrown. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get401_response import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response from a JSON string
rest_v10_companies_company_id_workflow_permanent_logs_get401_response_instance = RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_workflow_permanent_logs_get401_response_dict = rest_v10_companies_company_id_workflow_permanent_logs_get401_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response from a dict
rest_v10_companies_company_id_workflow_permanent_logs_get401_response_from_dict = RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response.from_dict(rest_v10_companies_company_id_workflow_permanent_logs_get401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


