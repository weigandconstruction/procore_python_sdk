# RestV10BimPlansGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_level_id** | **int** | ID of the BIM Level that the plan is associated to | [optional] 
**drawing_id** | **int** | ID of the Drawing that the plan is associated to | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**title** | **str** | Title of the plan. This reflects the title of the drawing associated to the plan. If plan is not associated to a drawing, the title will contain the associated location name | [optional] 
**image** | [**RestV10BimPlansGet200ResponseInnerAllOfImage**](RestV10BimPlansGet200ResponseInnerAllOfImage.md) |  | [optional] 
**thumbnail** | [**RestV10BimPlansGet200ResponseInnerAllOfThumbnail**](RestV10BimPlansGet200ResponseInnerAllOfThumbnail.md) |  | [optional] 
**sheet_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_plans_get200_response_inner import RestV10BimPlansGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimPlansGet200ResponseInner from a JSON string
rest_v10_bim_plans_get200_response_inner_instance = RestV10BimPlansGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BimPlansGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_bim_plans_get200_response_inner_dict = rest_v10_bim_plans_get200_response_inner_instance.to_dict()
# create an instance of RestV10BimPlansGet200ResponseInner from a dict
rest_v10_bim_plans_get200_response_inner_from_dict = RestV10BimPlansGet200ResponseInner.from_dict(rest_v10_bim_plans_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


