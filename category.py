def category_load():

    # truncate tmp table CATEGORY


        # truncate_tmp_category = '''
        #                             TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_CATEGORY
        #
        #                             '''

        # sf.execute_query(truncate_tmp_category)

#
    # load tmp table CATEGORY

        load_temp_category = '''
                                INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_CATEGORY(
                                CTGRY_ID,CTGRY_DESC
                                )
                                SELECT ID,CATEGORY_DESC
                                FROM BHATBHATENI.SASHANK_STG.STG_CATEGORY
                                '''
        sf.execute_query(load_temp_category)




    # load target table CATEGORY

        load_tgt_category = '''
                                INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_CATEGORY(
                                CTGRY_KY,CTGRY_ID,CTGRY_DESC,OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS
                                )
                                SELECT CTGRY_KY,CTGRY_ID, CTGRY_DESC,
                                1,LOCALTIMESTAMP,LOCALTIMESTAMP
                                FROM BHATBHATENI.SASHANK_TMP.TMP_CATEGORY
                                WHERE CTGRY_ID NOT IN (SELECT DISTINCT CTGRY_ID FROM BHATBHATENI.SASHANK_TGT.TGT_CATEGORY)
                                '''
        sf.execute_query(load_tgt_category)


        # update target table CATEGORY

        # update_tgt_category = '''
        #                             UPDATE BHATBHATENI.SASHANK_TGT.TGT_CATEGORY T1
        #                             SET T1.CTGRY_DESC = T2.CTGRY_DESC,
        #                             ROW_UPDT_TMS = LOCALTIMESTAMP
        #                             FROM BHATBHATENI.SASHANK_TMP.TMP_CATEGORY T2
        #                             WHERE T1.CTGRY_ID = T2.CTGRY_ID;
        #                             '''
        # sf.execute_query(update_tgt_category)
