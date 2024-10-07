# RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status in screaming snake case (like BAD_REQUEST) | [optional] 
**message** | **str** | Human readable message describing error. | [optional] 
**details** | [**List[RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner]**](RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseErrorDetailsInner.md) | Additional information about the error. | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error import RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError from a JSON string
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_instance = RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_dict = rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError from a dict
rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch400ResponseError.from_dict(rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch400_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


