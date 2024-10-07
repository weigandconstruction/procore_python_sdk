# RestV10ProjectsSyncPatchRequestUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**active** | **bool** | The project active status. | [optional] [default to True]
**address** | **str** | The street address of the project. | [optional] 
**city** | **str** | The city where the project is located. | [optional] 
**country_code** | **str** | The country code (ISO-3166 Alpha-2 format) where the project is located. | [optional] 
**description** | **str** | The project description. | [optional] 
**start_date** | **date** | The date that the contract for the project is signed. Note: This field replaces estimated_start_date and will mirror its value. | [optional] 
**completion_date** | **date** | The date that all parties agree the project meets or must meet “substantial completion”. Note: This field replaces estimated_completion_date and will mirror its value. | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: This field is a replacement of estimated_value and will mirror its value. | [optional] 
**warranty_start_date** | **date** | The project warranty start date. | [optional] 
**warranty_end_date** | **date** | The project warranty end date. | [optional] 
**flag** | **str** | The project flag. | [optional] 
**image_id** | **int** | The project image identifier. | [optional] 
**name** | **str** | The project name. | [optional] 
**office_id** | **int** | The project office identifier. | [optional] 
**phone** | **str** | The project telephone number. | [optional] 
**project_number** | **str** | The project number. | [optional] 
**public_notes** | **str** | The public notes for the project. | [optional] 
**project_stage_id** | **int** | The project stage identifier. | [optional] 
**square_feet** | **int** | The total square footage of the project. | [optional] 
**state_code** | **str** | The state code (ISO-3166 Alpha-2 format) where the project is located. | [optional] 
**time_zone** | **str** | The timezone where the project is located. | [optional] 
**zip** | **str** | The project postal code. | [optional] 
**program_id** | **int** | The project program identifier. | [optional] 
**project_bid_type_id** | **int** | The project bid type identifier. | [optional] 
**project_type_id** | **int** | The project type identifier. | [optional] 
**project_owner_type_id** | **int** | The project owner type identifier. | [optional] 
**project_region_id** | **int** | The project region id of the project. | [optional] 
**project_template_id** | **int** | The project template identifier as designated by another project on this company. It must be a project that is a template defined by &#x60;template: true&#x60;. | [optional] 
**origin_id** | **str** | External third-party identifier for the project. | [optional] 
**origin_data** | **str** | External third-party data string associated with the project. | [optional] 
**department_ids** | **List[int]** | The department ids the project is associated with. The array should represent all departments, so if the current value is &#x60;[1, 2, 3]&#x60; and want to remove department &#x60;2&#x60;, then send &#x60;[1, 3]&#x60;. | [optional] 
**estimated_value** | **float** | The estimated value of the project. Note: This field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**estimated_start_date** | **date** | The estimated start date of the project. Note: This field is now deprecated and will mirror the value of start_date until it is no longer supported. | [optional] 
**estimated_completion_date** | **date** | The estimated completion date of the project. Note: This field is now deprecated and will mirror the value of completion_date until it is no longer supported. | [optional] 
**store_number** | **str** | The project store number. | [optional] 
**accounting_project_number** | **str** | The project accounting project number. | [optional] 
**designated_market_area** | **str** | The project designated market area. | [optional] 
**enable_copy_of_standard_cost_codes** | **bool** | This property enables the user to copy default standard cost codes during new project creation when it is set to true. However, this flag does not have any impact when using project template, and the company&#39;s configuration is set to copy project template cost codes. | [optional] [default to False]

## Example

```python
from procore_sdk.models.rest_v10_projects_sync_patch_request_updates_inner import RestV10ProjectsSyncPatchRequestUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsSyncPatchRequestUpdatesInner from a JSON string
rest_v10_projects_sync_patch_request_updates_inner_instance = RestV10ProjectsSyncPatchRequestUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsSyncPatchRequestUpdatesInner.to_json())

# convert the object into a dict
rest_v10_projects_sync_patch_request_updates_inner_dict = rest_v10_projects_sync_patch_request_updates_inner_instance.to_dict()
# create an instance of RestV10ProjectsSyncPatchRequestUpdatesInner from a dict
rest_v10_projects_sync_patch_request_updates_inner_from_dict = RestV10ProjectsSyncPatchRequestUpdatesInner.from_dict(rest_v10_projects_sync_patch_request_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


