# RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**filename** | **str** | Filename | [optional] 
**coordinate_system** | **str** | Coordinate system used in exporting gridlines | [optional] 
**project_id** | **int** | Project ID | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**gridline_file** | [**RestV10ScheduleIntegrationGet200ResponseInnerFile**](RestV10ScheduleIntegrationGet200ResponseInnerFile.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline import RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline from a JSON string
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline_instance = RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline.to_json())

# convert the object into a dict
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline_dict = rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline_instance.to_dict()
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline from a dict
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline_from_dict = RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline.from_dict(rest_v10_bim_models_get200_response_inner_one_of1_current_revision_bim_gridline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


