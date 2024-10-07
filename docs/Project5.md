# Project5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The Active status of the project. Must be true or false. | [optional] [default to True]
**address** | **str** | The street address for the Project location | [optional] 
**city** | **str** | The City in which the project is located | [optional] 
**country_code** | **str** | The two character code that represents the country in which the project is located (ISO-3166 Alpha-2 format) | [optional] 
**county** | **str** | The County in which the project is located | [optional] 
**description** | **str** | The description for the project | [optional] 
**erp_integrated** | **bool** | This project is integrated with ERP | [optional] [default to False]
**standard_cost_code_list_id** | **int** | The identifier for the Standard Cost Code List | [optional] 
**start_date** | **date** | The date that the contract for the project is signed. Note: this field is a replacement to estimated_start_date and will mirror its value. | [optional] 
**completion_date** | **date** | The date that all parties agree the project meets or must meet “substantial completion”. Note: this field is a replacement to estimated_completion_date and will mirror its value. | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: this field is a replacement to estimated_value and will mirror its value. | [optional] 
**warranty_start_date** | **date** | The start date for the Project Warranty | [optional] 
**warranty_end_date** | **date** | The end date for the Project Warranty | [optional] 
**fax** | **str** | The fax number for the project | [optional] 
**flag** | **str** | The flag for the project | [optional] 
**image_id** | **int** | The identifier for the project image | [optional] 
**name** | **str** | The name of the project | [optional] 
**office_id** | **int** | The identifier for the Project Office | [optional] 
**phone** | **str** | The telephone number for the Project | [optional] 
**project_number** | **str** | The number for the Project | [optional] 
**public_notes** | **str** | The public notes for the Project | [optional] 
**project_stage_id** | **int** | The identifier for the Project Stage | [optional] 
**square_feet** | **int** | The total square footage of the Project | [optional] 
**state_code** | **str** | The code that represents the Project State (ISO-3166 Alpha-2 format) | [optional] 
**time_zone** | **str** | The timezone the Project is located in | [optional] 
**zip** | **str** | The postal code for the Project | [optional] 
**parent_job_id** | **int** | The identifier for the Project&#39;s Parent Job | [optional] 
**program_id** | **int** | The identifier for the Project Program ID | [optional] 
**project_bid_type_id** | **int** | The identifier for the Project Bid Type | [optional] 
**project_type_id** | **int** | The identifier for the Project Type | [optional] 
**project_owner_type_id** | **int** | The identifier for the Project Owner Type | [optional] 
**project_region_id** | **int** | The identifier for the Project Region | [optional] 
**project_template_id** | **int** | The identifier for the Project Template as designated by another Project on this company. It must be a Project that is a Template defined by template: &#x60;true&#x60; | [optional] 
**origin_id** | **str** | An external third-party identifier for the Project | [optional] 
**origin_data** | **str** | An external third-party data string associated with the Project | [optional] 
**origin_code** | **str** | An external third-party code associated with the Project | [optional] 
**department_ids** | **List[int]** | The identifiers for the Departments the Project belongs to. The array should always represent all Departments, so if you have &#x60;[1, 2, 3]&#x60; and want to remove deparment &#x60;2&#x60;, then send &#x60;[1, 3]&#x60; | [optional] 
**estimated_value** | **float** | The Estimated Value of the project. Note: this field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**estimated_start_date** | **date** | The Estimated Start Date of the Project Note: this field is now deprecated and will mirror the value of start_date until it is no longer supported. | [optional] 
**estimated_completion_date** | **date** | The Estimated Completion Date of the Project. Note: this field is now deprecated and will mirror the value of completion_date until it is no longer supported. | [optional] 
**store_number** | **str** | Store Number of the Project | [optional] 
**accounting_project_number** | **str** | Accounting Project Number of the Project | [optional] 
**designated_market_area** | **str** | Designated Market Area of the Project | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project5 import Project5

# TODO update the JSON string below
json = "{}"
# create an instance of Project5 from a JSON string
project5_instance = Project5.from_json(json)
# print the JSON string representation of the object
print(Project5.to_json())

# convert the object into a dict
project5_dict = project5_instance.to_dict()
# create an instance of Project5 from a dict
project5_from_dict = Project5.from_dict(project5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


