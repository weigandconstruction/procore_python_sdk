# RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** | A machine-readable code that identifies the error specifically enough for the client to interpret what happened and take action. | 
**message** | **str** | Human readable message | 
**source** | **str** | Source of the error | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner import RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner from a JSON string
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner_instance = RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner_dict = rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner from a dict
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner.from_dict(rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


