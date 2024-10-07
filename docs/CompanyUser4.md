# CompanyUser4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The First Name of the Company User | [optional] 
**last_name** | **str** | The Last Name of the Company User | 
**job_title** | **str** | The Job Title of the Company User | [optional] 
**address** | **str** | The Address of the Company User | [optional] 
**city** | **str** | The City of the Company User | [optional] 
**zip** | **str** | The Zip code of the Company User | [optional] 
**business_phone** | **str** | The Business Phone of the Company User | [optional] 
**business_phone_extension** | **int** | The Business Phone Extension of the Company User | [optional] 
**mobile_phone** | **str** | The Mobile Phone of the Company User | [optional] 
**fax_number** | **str** | The Fax Number of the Company User | [optional] 
**email_address** | **str** | The Email Address of the Company User. Update requests including this parameter will be rejected unless the requesting user has Directory Admin permissions | 
**email_signature** | **str** | The Email Signature of the Company User | [optional] 
**is_active** | **bool** | The Active status of the Company User | [optional] 
**is_employee** | **bool** | The Employee status of the Company User | [optional] [default to False]
**employee_id** | **str** | The ID of the Employee of the Company User when &#x60;user[is_employee]&#x60; is set to &#x60;true&#x60; | [optional] 
**notes** | **str** | The Notes (notes, keywords, tags) of the Company User | [optional] 
**country_code** | **str** | The Country Code of the Company User (ISO-3166 Alpha-2 format) | [optional] 
**state_code** | **str** | The State Code of the Company User (ISO-3166 Alpha-2 format) | [optional] 
**initials** | **str** | The Initials of the Company User | [optional] 
**origin_id** | **str** | The Origin ID of the Company User | [optional] 
**origin_data** | **str** | The Origin Data of the Company User | [optional] 
**vendor_id** | **int** | The ID of the Vendor of the Company User | [optional] 
**default_permission_template_id** | **int** | The ID of the default Permission Template for the Company User. Requests including this parameter will be rejected unless the requesting user has Directory Admin permissions | [optional] 
**company_permission_template_id** | **int** | The ID of the Company Permission Template for the Company User. Requests including this parameter will be rejected unless the requesting user has Directory Admin permissions | [optional] 
**work_classification_id** | **int** | The ID of the Work Classification for the Company User | [optional] 
**avatar** | **str** | The Avatar of the Company User. To upload avatar you must upload whole payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;user[avatar]&#x60; as file. | [optional] 

## Example

```python
from procore_sdk.models.company_user4 import CompanyUser4

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUser4 from a JSON string
company_user4_instance = CompanyUser4.from_json(json)
# print the JSON string representation of the object
print(CompanyUser4.to_json())

# convert the object into a dict
company_user4_dict = company_user4_instance.to_dict()
# create an instance of CompanyUser4 from a dict
company_user4_from_dict = CompanyUser4.from_dict(company_user4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


